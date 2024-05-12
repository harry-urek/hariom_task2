import json
import logging

# Configure logging
logging.basicConfig(filename='processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def filter_questions(questions, difficulty_level=None, tags=None):
    filtered_questions = []
    for question in questions:
        if difficulty_level and question['difficulty_level'] != difficulty_level:
            continue
        if tags and not any(tag in question['tags'] for tag in tags):
            continue
        filtered_questions.append(question)
    return filtered_questions


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
    try:
        # Read data from the JSON file
        with open('questions.json', 'r') as file:
            data = json.load(file)
            questions = data['questions']

        # Filter questions based on difficulty level or tags
        difficulty_level = input(
            "Enter the difficulty level to filter (easy, medium, hard), or leave blank for all: ").lower()
        tags = input(
            "Enter the tags to filter (comma-separated), or leave blank for all: ").lower().split(',')
        tags = [tag.strip() for tag in tags if tag.strip()]

        filtered_questions = filter_questions(
            questions, difficulty_level if difficulty_level else None, tags if tags else None)

        # Group the filtered questions by attributes
        grouped_questions = group_questions_by_attributes(filtered_questions)

        # Save the grouped questions to a new file
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
