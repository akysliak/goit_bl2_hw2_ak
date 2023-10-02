To build an image run:

    docker build . -t cli-ab
    
To run the container:
    
    docker run -it cli-ab

Within the container, run:

    python address_book/main.py
