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

@dataclass
class ReactorStatusMapping:
    """Data class to store the different reactor status values."""
    low: str = 'LOW'
    normal: str = 'NORMAL'
    danger: str = 'DANGER'

@dataclass
class ReactorStatus:
    """Data class to hold the status thresholds and logic to assess reactor status."""
    low_threshold_pct: float = 0.9    # 90% of the threshold
    normal_threshold_pct: float = 1.0 # +/- 10% of the threshold
    high_threshold_pct: float = 1.1   # 110% of the threshold
    status_mapping: ReactorStatusMapping = ReactorStatusMapping()

    def assess_status(self, product: Union[int, float], threshold: Union[int, float]) -> str:
        """Assess reactor status based on the product of temperature and neutrons per second."""
        if product < threshold * self.low_threshold_pct:
            return self.status_mapping.low
        elif threshold * self.low_threshold_pct <= product <= threshold * self.high_threshold_pct:
            return self.status_mapping.normal
        else:
            return self.status_mapping.danger


# Instantiate the data classes with default values
CRITICALITY_BALANCE_CONDITIONS = CriticalityBalanceConditions()
EFFICIENCY_ZONES = ReactorEfficiencyZones()
REACTOR_STATUS = ReactorStatus()

def is_criticality_balanced(temperature: Union[int, float], neutrons_emitted: Union[int, float]) -> bool:
    # TODO: add exceptions
    """
    Checks if reactor is balanced.

    Params:
        temperature (int or float) - temperature value in kelvin.
        neutrons_emitted (int or float) - number of neutrons emitted per second.
    Returns:
        bool - is criticality balanced?
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
        str - reactor efficiency zone ('green', 'orange', 'red', or 'black').
    """
    generated_power = voltage * current
    efficiency_pct = (generated_power / theoretical_max_power) * 100
    return EFFICIENCY_ZONES.get_efficiency_zone(efficiency_pct)


def fail_safe(temperature: Union[int, float], neutrons_produced_per_second: Union[int, float], threshold: Union[int, float]) -> str:
    #TODO: add exceptions
    """
    Assess and return status code for the reactor.

    Params:
        temperature (int or float) - value of the temperature in kelvin.
        neutrons_produced_per_second (int or float) - neutron flux.
        threshold (int or float) - threshold for category.
    Returns:
        str - fail-safe status code.
    """

    # Calculate the product of temperature and neutrons emitted
    product = temperature * neutrons_produced_per_second

    # Use ReactorStatus to assess the status based on the threshold
    return REACTOR_STATUS.assess_status(product, threshold)