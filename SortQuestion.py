import json
import logging


def group_questions_by_attributes(questions):
    grouped_questions = {
        'hard': [],
        'medium': [],
        'easy': [],
        'graph': [],
        'two_pointer': [],
        'sorting': [],
        'string': [],
        'array': [],
        'dynamic_programming': [],
        'breadth_first_search': [],
        'sliding_window': [],
        'hash_table': [],
        'binary_tree': []
    }

    for question in questions:
        difficulty_level = question['difficulty_level']
        tags = question['tags']

        if difficulty_level == 'hard':
            grouped_questions['hard'].append(question)
        elif difficulty_level == 'medium':
            grouped_questions['medium'].append(question)
        elif difficulty_level == 'easy':
            grouped_questions['easy'].append(question)

        for tag in tags:
            if tag == 'graph':
                grouped_questions['graph'].append(question)
            elif tag == 'two_pointers':
                grouped_questions['two_pointer'].append(question)
            elif tag == 'sorting':
                grouped_questions['sorting'].append(question)
            elif tag == 'string':
                grouped_questions['string'].append(question)
            elif tag == 'array':
                grouped_questions['array'].append(question)
            elif tag == 'dynamic_programming':
                grouped_questions['dynamic_programming'].append(question)
            elif tag == 'breadth_first_search':
                grouped_questions['breadth_first_search'].append(question)

    return grouped_questions


def main():
    pass
