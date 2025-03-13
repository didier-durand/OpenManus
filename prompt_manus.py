import asyncio

from app.agent.manus import Manus
from app.logger import logger

from pydantic import BaseModel, Field

class Prompt(BaseModel):
    pass


def bullet_list(str_list=None):
    if str_list is None:
        str_list = []
    list_str = "\n"
    if len(str_list) > 0:
        for bullet in str_list:
            list_str += f"* {bullet} \n"
    return list_str


class CodePrompt(Prompt):
    field: str = Field(default="")
    guidance: str = Field(
        default="You are an expert Python full-stack developer. Your mission is to execute the tasks below explained "
                "in section named TASKS while respecting the rules defined in section RULES.")

    tasks: list[str] = Field(
        default=[])
    rules: list[str] = Field(
        default=[
        "When you generate PYTHON code, enclose it with ```python at beginning and at end.",
        "When you generate JSON code, enclose it with ```json at beginning and at end.",
        "When you generate YAML code, enclose it with ```yaml at beginning and at end.",
        "When you generate MARKDOWN text, enclose it with ```md at beginning and at end.",
        "When you generate JAVASCRIPT text, enclose it with ```js at beginning and at end.",
        "When you generate TYPESCRIPT text, enclose it with ```ts at beginning and at end.",
    ])

    def __repr__(self):
        return (self.guidance.strip("\n")
                + "\nTASKS:\n"
                + bullet_list(self.tasks)
                + "\nRULES:\n"
                + bullet_list(self.rules))

    def __str__(self):
        return self.__repr__()

async def prompt_manus(prompt: str = ""):
    agent = Manus() # noqa
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
    request = CodePrompt()
    request.tasks = [
        "generate a Python program",
        "generate a JSON data structure",
    ]
    print(str(request))
    asyncio.run(prompt_manus(str(request)))

