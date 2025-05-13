import asyncio
import logging
import os

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from api import AssistantFnc

load_dotenv()

# Configure logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger("Genesis")

# Validate required envs
REQUIRED_ENVS = ["LIVEKIT_URL", "LIVEKIT_API_KEY", "LIVEKIT_API_SECRET", "OPENAI_API_KEY"]
for var in REQUIRED_ENVS:
    if not os.getenv(var):
        raise RuntimeError(f"Environment variable `{var}` not set.")


async def entrypoint(ctx: JobContext):
    logger.info("Genesis assistant starting...")

    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are Genesis, a voice assistant created by LiveKit. "
            "Communicate clearly, concisely, and without unpronounceable punctuation."
        ),
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = AssistantFnc()

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx,
    )

    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hey, how can I help you today!", allow_interruptions=True)

    try:
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        logger.info("Genesis assistant shutting down.")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
