import re


def find_zip(file_path):
    extensions = re.compile(r"""
        \.zip|\.rar|\.gz|\.tar|\.7z|\.bz2|\.tgz|
        \.swp|\.backup|\.vbs|\.inc|\.ini|
        \.sql|\.old|\.conf|
        \.svn|\.git""", re.X)

    try:
        match = extensions.search(file_path)
        if match:
            print(file_path)
    except Exception as e:
        pass


def main():
    file_path = r"/Users/wangwei/PycharmProjects/untitled.zip"
    find_zip(file_path)


if __name__ == '__main__':
    main()
