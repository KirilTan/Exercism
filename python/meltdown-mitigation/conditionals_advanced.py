from dataclasses import dataclass
from typing import Union

@dataclass
class CriticalityBalanceConditions:
    """
    Data class to hold criticality balance conditions for a nuclear reactor.

    Attributes:
        critical_temperature_limit (int)
            The maximum temperature limit in kelvin for the reactor to be considered criticality balanced.
        min_neutrons_emitted_per_second (int)
            The minimum number of neutrons emitted per second for the reactor to be considered criticality balanced.
        max_product_temperature_neutrons: (int)
            The maximum product of temperature and neutrons emitted per second for the reactor to be considered criticality balanced.
    """
    critical_temperature_limit: int = 800
    min_neutrons_emitted_per_second: int = 500
    max_product_temperature_neutrons: int = 500000

@dataclass
class EfficiencyBand:
    """
    A data class to represent an efficiency band for a nuclear reactor.

    Attributes:
        threshold (int): The threshold value for the efficiency percentage.
        output (str): The efficiency zone output.
    """
    threshold: int
    output: str

@dataclass
class ReactorEfficiencyZones:
    green: EfficiencyBand = EfficiencyBand(
        threshold=80,
        output="green"
    )
    orange: EfficiencyBand = EfficiencyBand(
        threshold=60,
        output="orange"
    )
    red: EfficiencyBand = EfficiencyBand(
        threshold=30,
        output="red"
    )
    black: EfficiencyBand = EfficiencyBand(
        threshold=0,
        output="black"
    )

    def get_efficiency_zone(self, efficiency_pct: float) -> str:
        """
        Return the efficiency zone based on the calculated efficiency percentage.

        Parameters:
            efficiency_pct (float): The calculated efficiency percentage.

        Returns:
            str: The efficiency zone ('green', 'orange', 'red', or 'black').

        The efficiency zone is determined by comparing the efficiency percentage to the threshold values
        defined in the EfficiencyBand instances. If the efficiency percentage is greater than or equal to
        the threshold of a band, that band's output is returned. If the efficiency percentage is less than
        the threshold of all bands, the output of the 'black' band is returned.
        """
        for band in [self.green, self.orange, self.red]:
            if efficiency_pct >= band.threshold:
                return band.output
        return self.black.output

# Instantiate the data classes with default values
CRITICALITY_BALANCE_CONDITIONS = CriticalityBalanceConditions()
EFFICIENCY_ZONES = ReactorEfficiencyZones()

def is_criticality_balanced(temperature: Union[int, float], neutrons_emitted: Union[int, float]) -> bool:
    # TODO: add exceptions
    """
    Checks if reactor is balanced.

    Params:
        temperature (int or float) - temperature value in kelvin.
        neutrons_emitted (int or float) - number of neutrons emitted per second.
    Returns:
        bool - is criticality balanced?

    Example:
        >>> is_criticality_balanced(750, 600)
        True
    """
    return (
            temperature < CRITICALITY_BALANCE_CONDITIONS.critical_temperature_limit and
            neutrons_emitted > CRITICALITY_BALANCE_CONDITIONS.min_neutrons_emitted_per_second and
            temperature * neutrons_emitted < CRITICALITY_BALANCE_CONDITIONS.max_product_temperature_neutrons
    )

def reactor_efficiency(voltage: Union[int, float], current: Union[int, float], theoretical_max_power: Union[int, float]) -> str:
    # TODO: add exceptions
    """
    Assess reactor efficiency zone.

    Params:
        voltage (int or float) - voltage value.
        current: (int or float) - current value.
        theoretical_max_power (int or float) - power that corresponds to a 100% efficiency.
    Returns:
        str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current

    Example:
        >>> reactor_efficiency(200, 50, 15000)
        'orange'
    """
    generated_power = voltage * current
    efficiency_pct = (generated_power / theoretical_max_power) * 100
    return EFFICIENCY_ZONES.get_efficiency_zone(efficiency_pct)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
