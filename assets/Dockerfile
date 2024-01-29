ARG FUNCTION_DIR=/functions

FROM public.ecr.aws/docker/library/python:3.11-slim-bullseye
ARG FUNCTION_DIR

RUN apt update -y && apt upgrade -y
RUN mkdir -p ${FUNCTION_DIR}

RUN pip install --target ${FUNCTION_DIR} awslambdaric
RUN pip install nbconvert && apt install -y pandoc &&\
    apt clean && rm -rf /var/lib/apt/lists/*
COPY app.py ${FUNCTION_DIR}

WORKDIR ${FUNCTION_DIR}
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]