ARG FUNCTION_DIR=/functions

FROM public.ecr.aws/debian/debian:stable-slim
ARG FUNCTION_DIR

RUN apt update -y && apt upgrade -y
RUN apt install -y python3 python3-pip jupyter python3-nbconvert &&\
    apt clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR}
RUN pip install --target ${FUNCTION_DIR} awslambdaric
COPY ./notebooks/ ./notebooks/
COPY app.py ./

ENTRYPOINT [ "/usr/bin/python3", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]