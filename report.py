import argparse
import io

from google.cloud import vision


def annotate(path):
    """Returns web annotations given the path to an image."""
    image = None
    vision_client = vision.Client()

    if path.startswith('http') or path.startswith('gs:'):
        image = vision_client.image(source_uri=path)

    else:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision_client.image(content=content)

    return image.detect_web()


def report(annotations):
    """Prints detected features in the provided web annotations."""
    if annotations.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in annotations.pages_with_matching_images:
            print('Score : {}'.format(page.score))
            print('Url   : {}'.format(page.url))

    if annotations.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(annotations.full_matching_images)))

        for image in annotations.full_matching_images:
            print('Score:  {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if annotations.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(annotations.partial_matching_images)))

        for image in annotations.partial_matching_images:
            print('Score: {}'.format(image.score))
            print('Url  : {}'.format(image.url))

    if annotations.web_entities:
        print ('\n{} Web entities found: '.format(
            len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    path_help = str('The image to detect, can be web URI, '
                    'Google Cloud Storage, or path to local file.')
    parser.add_argument('image_url', help=path_help)
    args = parser.parse_args()

    report(annotate(args.image_url))