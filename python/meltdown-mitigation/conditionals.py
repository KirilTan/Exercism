from dataclasses import dataclass, field
from typing import Union

@dataclass
class CriticalityBalanceConditions:
    """
    Data class to hold criticality balance conditions for a nuclear reactor.
    """
    critical_temperature_limit: int = 800
    min_neutrons_emitted_per_second: int = 500
    max_product_temperature_neutrons: int = 500000

@dataclass
class EfficiencyBand:
    """
    A data class to represent an efficiency band for a nuclear reactor.
    """
    threshold: int
    output: str

@dataclass
class ReactorEfficiencyZones:
    green: EfficiencyBand = field(default_factory=lambda: EfficiencyBand(threshold=80, output="green"))
    orange: EfficiencyBand = field(default_factory=lambda: EfficiencyBand(threshold=60, output="orange"))
    red: EfficiencyBand = field(default_factory=lambda: EfficiencyBand(threshold=30, output="red"))
    black: EfficiencyBand = field(default_factory=lambda: EfficiencyBand(threshold=0, output="black"))

    def get_efficiency_zone(self, efficiency_pct: float) -> str:
        """
        Return the efficiency zone based on the calculated efficiency percentage.
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
    status_mapping: ReactorStatusMapping = field(default_factory=ReactorStatusMapping)

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
    """
    Checks if reactor is balanced.
    """
    return (
            temperature < CRITICALITY_BALANCE_CONDITIONS.critical_temperature_limit and
            neutrons_emitted > CRITICALITY_BALANCE_CONDITIONS.min_neutrons_emitted_per_second and
            temperature * neutrons_emitted < CRITICALITY_BALANCE_CONDITIONS.max_product_temperature_neutrons
    )

def reactor_efficiency(voltage: Union[int, float], current: Union[int, float], theoretical_max_power: Union[int, float]) -> str:
    """
    Assess reactor efficiency zone.
    """
    generated_power = voltage * current
    efficiency_pct = (generated_power / theoretical_max_power) * 100
    return EFFICIENCY_ZONES.get_efficiency_zone(efficiency_pct)


def fail_safe(temperature: Union[int, float], neutrons_produced_per_second: Union[int, float], threshold: Union[int, float]) -> str:
    """
    Assess and return status code for the reactor.
    """
    product = temperature * neutrons_produced_per_second
    return REACTOR_STATUS.assess_status(product, threshold)
