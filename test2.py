import logging
import requests

logging.basicConfig(level=logging.INFO)

class web_search:

    def inference(self, newprompt, max_context):
        response_parts = newprompt.split('### Response:')
        if len(response_parts) < 2:
            return newprompt
        response = response_parts[-1]
        search_index = response.find('[search:')

        if search_index == -1:
            is_search = response.find('[search:')

            if is_search == -1:
                return newprompt

        query = response.split('[search:')[1].split(']')[0].strip()
        query = query.replace(' ', '+')
        logging.info(f'query: {query}')
        try:
            response.raise_for_status()
            json_object = response.json()
            if len(json_object['Abstract']) > 0:
                result = json_object['Abstract']
            elif len(json_object['RelatedTopics']) > 0:
                result = json_object['RelatedTopics'][0]['Text']
            else:
                result = 'No results found'
        except requests.RequestException as e:
            logging.error(f'Network error occurred: {e}')
            return newprompt
        except (KeyError, IndexError) as e:
            logging.error(f'Parsing error occurred: {e}')
            return newprompt
        if len(newprompt) > max_new_prompt:
            newprompt = newprompt[-max_new_prompt:]
        else:
            newprompt = newprompt
            return newprompt
        result_length = len(result)
        max_new_prompt = max_context-result_length

        newprompt = (newprompt[-(max_new_prompt):]) if len(newprompt) > max_new_prompt else newprompt
        return f'Search result:[{result}] {newprompt}'
    
print(web_search().inference('### Response: [search: Python] Python is a programming language', 100))