import enum
import logging
from typing import Annotated
from livekit.agents import llm

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

    def __str__(self):
        return self.value.replace("_", " ").title()


class AssistantFnc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }

    @llm.ai_callable(description="Get the temperature in a specific room")
    def get_temperature(
        self, zone: Annotated[Zone, llm.TypeInfo(description="The specific zone to check")]
    ) -> str:
        logger.info("Getting temperature for zone: %s", zone)
        temp = self._temperature.get(zone)
        return f"The temperature in the {zone} is {temp}°C." if temp else f"No temperature data for {zone}."

    @llm.ai_callable(description="Set the temperature in a specific room")
    def set_temperature(
        self,
        zone: Annotated[Zone, llm.TypeInfo(description="The specific zone to adjust")],
        temp: Annotated[int, llm.TypeInfo(description="The temperature to set (in °C)")],
    ) -> str:
        logger.info("Setting temperature for zone: %s to %s°C", zone, temp)
        self._temperature[zone] = temp
        return f"The temperature in the {zone} is now set to {temp}°C."
