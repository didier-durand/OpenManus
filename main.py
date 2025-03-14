import argparse
import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main(prompt: str = ""):
    agent = Manus()
    try:
        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--prompt", type=str,help="task prompt for OpenManus")
    args = parser.parse_args()
    if args.prompt is not None:
        user_prompt = args.prompt
    else:
        user_prompt = input("Enter your prompt:")
    asyncio.run(main(prompt=user_prompt))
