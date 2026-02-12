import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class AITicketWorkflow:
    def __init__(self):
        self.state = 0  # Start at the initial state
        self.max_state = 9  # Define the last state of the workflow

    def validate_token(self, token):
        logging.debug('Validating token...')
        # Placeholder for token validation logic
        if token == 'valid_token':
            logging.info('Token is valid.')
            return True
        logging.error('Invalid token!')
        return False

    def check_data(self, data):
        logging.debug('Checking data...')
        # Placeholder for data checking logic
        if data:
            logging.info('Data is valid.')
            return True
        logging.error('Invalid data!')
        return False

    def transition_to_next_state(self):
        if self.state < self.max_state:
            logging.info(f'Transitioning from state {self.state} to {self.state + 1}')
            self.state += 1
            logging.debug(f'Current state: {self.state}')
            return self.state
        logging.error('Cannot transition. Already at the maximum state.');
        return None

    def process_ticket(self, token, data):
        if not self.validate_token(token):
            raise Exception('Token validation failed.')
        if not self.check_data(data):
            raise Exception('Data check failed.')

        for i in range(10):
            logging.info(f'Processing state {self.state}')
            time.sleep(1)  # Simulate processing time
            self.transition_to_next_state()

if __name__ == '__main__':
    workflow = AITicketWorkflow()
    workflow.process_ticket('valid_token', 'sample_data')
    logging.info('Workflow completed successfully.');
