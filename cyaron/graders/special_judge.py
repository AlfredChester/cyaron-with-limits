from ..utils import *
from .grader_registry import CYaRonGraders
from .mismatch import TextMismatch
import os
import subprocess


def __generate_temp_file(content: str):
    name = "cyaron_temp_file_" + os.urandom(16).hex() + ".txt"
    return open(name, "w")


def testlib_spj(spj_program: str) -> str:
    """
    Returns a grader identifier with the given testlib spj executive.

    This function takes a string, generates a recognizable grader instance
    and returns the identifier of the grader for Compare.program to use.
    e.g. Compare.program("a.exe", input=input_io, std_program="std.exe", grader=testlib_spj("spj.exe"))
    Args:
        spj_program: The path of the spj executive.
    Returns:
        str: the identifier of the grader.
    """
    grader_id = "testlib_spj_" + os.urandom(8).hex()

    @CYaRonGraders.grader(grader_id)
    def grader_impl(input_file, output, answer):
        # input is a filename
        # output and answer are content.
        # TODO figure out a better implementation
        output_file = __generate_temp_file(output)
        answer_file = __generate_temp_file(answer)
        res = subprocess.run(
            "{} {} {} {}".format(spj_program, input_file, output_file, answer_file),
            stdout=subprocess.PIPE,
            universal_newlines=True,
            text=True,
        )
        output_file.close()
        answer_file.close()
        if res.returncode == 0:
            return True, None
        else:
            return False, make_unicode(res.stdout)

    return grader_id


# TODO implement spj support for more OJs.
