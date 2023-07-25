import mandrill
import base64

# Your Mandrill API key
MANDRILL_API_KEY = 'hnYCG2OcRIiKrcdQBHRohA'

# read local file to attach emails
def read_file_content(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def send_email_with_attachment(subject, message, from_email, to_email, attachment_filename, attachment_content):
    try:
        mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)

        attachment = {
            'type': 'application/octet-stream',  # Adjust the MIME type according to the file being attached
            'name': attachment_filename,
            'content': base64.b64encode(attachment_content).decode()
        }

        message = {
            'from_email': from_email,
            'to': [{'email': to_email, 'type': 'to'}],
            'subject': subject,
            'html': message,
            'attachments': [attachment]
        }

        result = mandrill_client.messages.send(message=message)
        print("Email with attachment sent successfully!")
        print(result)

    except mandrill.Error as e:
        print(f"A Mandrill error occurred: {e}")

# Usage example
if __name__ == "__main__":
    subject = "Crawling MagicMillions catalogues"
    message = "<p>Please, refer attached file.</p>"
    from_email = "system@bloodstockauction.com"
    to_email = "it@bloodstockauction.com"

    # Example attachment file path
    file_path = './result-11-07-2023.csv'
    attachment_filename = 'result-11-07-2023.csv'
    attachment_content = read_file_content(file_path)

    send_email_with_attachment(subject, message, from_email, to_email, attachment_filename, attachment_content)
