from dataclasses import dataclass
from typing import Callable, Dict, Tuple

@dataclass
class BobResponses:
    """Represents Bob's responses to various types of sentences."""
    silence: str = "Fine. Be that way!"
    yell: str = "Whoa, chill out!"
    question: str = "Sure."
    yell_question: str = "Calm down, I know what I'm doing!"
    everything_else: str = "Whatever."


@dataclass
class SentenceType:
    """Represents the type of sentence based on its properties."""
    is_question: bool
    is_yelling: bool
    is_silence: bool

    @classmethod
    def from_sentence(cls, sentence: str) -> "SentenceType":
        """Determine the sentence type properties based on the content of the sentence."""
        stripped_sentence = sentence.strip()
        return cls(
            is_question=stripped_sentence.endswith('?'),
            is_yelling=stripped_sentence.isupper(),
            is_silence=(stripped_sentence == "")
        )


@dataclass
class ResponseMapper:
    """Maps sentence types to their corresponding responses."""
    response_map: Dict[Tuple[bool, bool, bool], Callable[[], str]]

    @classmethod
    def default(cls) -> "ResponseMapper":
        """Creates a default mapper with predefined response mappings."""
        return cls(
            response_map={
                (False, False, True): lambda: BobResponses.silence,
                (True, True, False): lambda: BobResponses.yell_question,
                (True, False, False): lambda: BobResponses.question,
                (False, True, False): lambda: BobResponses.yell,
                (False, False, False): lambda: BobResponses.everything_else,
            }
        )

    def get_response(self, sentence_type: SentenceType) -> str:
        """Fetch the response based on the sentence type properties."""
        key = (sentence_type.is_question, sentence_type.is_yelling, sentence_type.is_silence)
        return self.response_map.get(key, lambda: BobResponses.everything_else)()


def response(sentence: str) -> str:
    """Determines Bob's response based on the type of sentence provided."""
    sentence_type = SentenceType.from_sentence(sentence)
    response_mapper = ResponseMapper.default()
    return response_mapper.get_response(sentence_type)
