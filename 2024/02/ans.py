from __future__ import annotations
from pathlib import Path
"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces.


This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

--- 
Assumptions:
* I need to find the total NUMBER of safe reports
* Need to be able to tell if all numbers are decreasing or increasing or neither
* Need to be able to tell if N and N+1 are within a range of 1,3

--- 
Approach:
* Function for increase/decrease. Only consider these reports
* Function for in_range.
* Return length of output
"""

def is_increasing(report: list[int]) -> bool:
    return all(report[position] < report[position + 1] for position in range(len(report) - 2))

def is_decreasing(report: list[int]) -> bool:
    return all(report[position] > report[position + 1] for position in range(len(report) - 2))

def is_in_safe_range(report: list[int], safe_range: tuple[int, int] = (1,3)) -> bool:
    for position, level in enumerate(report[:len(report) - 1]):
        safe_levels = list(range(level + safe_range[0], level + safe_range[1] + 1 ))
        if not report[position + 1] in safe_levels:
            return False
    return True

reports = []
with Path("input.txt").open("r") as question_input:
    for line in question_input.readlines():
        reports.append([int(level) for level in line.strip().split(" ")])

safe_reports = [
    report for report in reports if (
        (is_increasing(report=report) and is_in_safe_range(report=report)) or
        (is_decreasing(report=report) and is_in_safe_range(report=report[::-1]))
    )
]
print(len(safe_reports))



"""
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
---
Assumptions:
* If I need to drop more than one number from a report then its faulty
* Need to rework the is_increasing and is_decreasing and is_in_safe_range functions.
Approach:
* If there is a removal and no flag set, continue. Set removal flag
* If there is a removal and flag set, return false
* Maintain existing logic


Below doesn't work because considering only neighbours for removal doesn't cover all cases
"""

def is_report_safe(report: list[int]) -> bool:
    dampened = False

    def check_with_dampener(
        local_report: list[int],
        conditional,
    ) -> bool:
        nonlocal dampened
        nonlocal report

        for position, left_level in enumerate(local_report[:len(local_report) - 1]):
            right_level = local_report[position + 1]
            if not conditional(left_level, right_level) or abs(left_level - right_level) not in [1,2,3]:
                if dampened:
                    return False
                dampened = True
                right_removed = local_report[::]
                right_removed.remove(right_level)

                left_removed = local_report[::]
                left_removed.remove(left_level)
                return (
                        check_with_dampener(local_report=right_removed, conditional=conditional) or
                        check_with_dampener(local_report=left_removed, conditional=conditional)
                )
        report = local_report
        return True

    def is_increasing() -> bool:
        nonlocal report
        nonlocal dampened
        dampened = False
        return check_with_dampener(local_report=report, conditional=lambda left, right: left < right)

    def is_decreasing() -> bool:
        nonlocal report
        nonlocal dampened
        dampened = False
        import pdb; pdb.set_trace()
        return check_with_dampener(local_report=report, conditional=lambda left, right: left > right)

    return is_increasing() or is_decreasing()


safe_reports_part_two = sum(
        any(
            (
                is_increasing(
                    report=report[:i] + report[i + 1:]
                ) and 
                is_in_safe_range(
                    report=report[:i] + report[i + 1:]
                )
            ) or
            (
                is_decreasing(
                    report=report[:i] + report[i + 1:]
                ) and 
                is_in_safe_range(
                    report=(report[:i] + report[i + 1:])[::-1]
            )
        ) for i in range(len(report))) for report in reports
)
print(safe_reports_part_two)
