from typing import Dict, List
from prompttools.experiment.openai_chat_experiment import OpenAIChatExperiment
from prompttools.harness.system_prompt_harness import SystemPromptExperimentationHarness

# Define a list of chat histories over which to run your experiment
system_prompts = ["You are a helpful assistant."]
user_inputs = ["Who won the world series in 2020?"]


# Define an evaluation function that assigns scores to each inference
def eval_fn(messages: List[Dict[str, str]], results: List[str]) -> float:
    for result in results:
        if "Dodgers" in result:
            return 1.0
    return 0.0


# Define an experimentation harness using the class name for the underlying experiment
harness = SystemPromptExperimentationHarness(
    OpenAIChatExperiment, "gpt-3.5-turbo", system_prompts, user_inputs
)

# Run the evaluation
harness.prepare()
harness.run()
harness.evaluate(eval_fn)
harness.visualize(pivot=True)