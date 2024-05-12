import json
import logging

# Configure logging
logging.basicConfig(filename='processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def filter_questions(questions, difficulty_level=None, tags=None):
    """
    The function `filter_questions` filters a list of questions based on specified difficulty level and
    tags.

    :param questions: The `questions` parameter is a list of dictionaries, where each dictionary
    represents a question. Each question dictionary likely contains information such as the question
    text, difficulty level, and tags associated with the question
    :param difficulty_level: The `difficulty_level` parameter in the `filter_questions` function is used
    to filter questions based on their difficulty level. If a difficulty level is provided, only
    questions with that specific difficulty level will be included in the filtered list. If no
    difficulty level is provided (i.e., `None`),
    :param tags: The `tags` parameter in the `filter_questions` function is used to filter questions
    based on specific tags. It allows you to specify one or more tags, and only questions that have at
    least one of the specified tags will be included in the filtered result
    :return: The function `filter_questions` returns a list of questions that match the specified
    difficulty level and tags criteria. If no criteria are specified (difficulty level and tags are both
    None), all questions are returned.
    """
    filtered_questions = []
    for question in questions:
        if difficulty_level and question['difficulty_level'] != difficulty_level:
            continue
        if tags and not any(tag in question['tags'] for tag in tags):
            continue
        filtered_questions.append(question)
    return filtered_questions


def group_questions_by_attributes(questions):
    """
    The function `group_questions_by_attributes` categorizes a list of questions based on their
    difficulty level and tags into different groups.

    :param questions: It looks like you are trying to group a list of questions based on their
    attributes such as difficulty level and tags. The function `group_questions_by_attributes` takes a
    list of questions as input and categorizes them into different groups based on their difficulty
    level and tags
    :return: The function `group_questions_by_attributes` returns a dictionary where questions are
    grouped based on their difficulty level and tags. The keys in the dictionary represent different
    attributes such as difficulty level ('hard', 'medium', 'easy') and tags ('graph', 'two_pointer',
    'sorting', 'string', 'array', 'dynamic_programming', 'breadth_first_search', 'sliding_window', 'hash
    """
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
    """
    The main function reads questions from a JSON file, filters them based on difficulty level and tags,
    groups them by attributes, and saves the grouped questions to a new JSON file.
    """

    try:
        with open('questions.json', 'r') as file:
            data = json.load(file)
            questions = data['questions']

        difficulty_level = input(
            "Enter the difficulty level to filter (easy, medium, hard), or leave blank for all: ").lower()
        tags = input(
            "Enter the tags to filter (comma-separated), or leave blank for all: ").lower().split(',')
        tags = [tag.strip() for tag in tags if tag.strip()]

        filtered_questions = filter_questions(
            questions, difficulty_level if difficulty_level else None, tags if tags else None)

        grouped_questions = group_questions_by_attributes(filtered_questions)

        with open('grouped_questions.json', 'w') as file:
            json.dump(grouped_questions, file, indent=4)

        logging.info('Questions grouped and saved to grouped_questions.json')
    except FileNotFoundError:
        logging.error('Error: questions.json file not found')
    except json.JSONDecodeError:
        logging.error('Error: Invalid JSON format in questions.json')
    except Exception as e:
        logging.error(f'Error: {str(e)}')


if __name__ == '__main__':
    main()
