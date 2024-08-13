FROM python:3.9-bullseye as BUILDER
COPY target/dist/my-quart-api*/dist/my_quart_api-*-py3-none-any.whl /tmp
COPY requirements.txt /tmp/
RUN python3 -m venv /venv \
    && . /venv/bin/activate && /venv/bin/python3 -m pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt && pip install /tmp/my_quart_api-*-py3-none-any.whl \
    && groupadd -g 1001 -r appuser && useradd -u 1001 -r -m -g appuser appuser

FROM python:3.9-bullseye as RUNTIME
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"
ENV LD_LIBRARY_PATH="/lib"
ENV SERVER_PORT=10002
COPY --from=BUILDER /venv /venv
COPY --from=BUILDER /lib /lib
EXPOSE 10002
WORKDIR /venv/bin
USER 1001
ENTRYPOINT ["python", "main.py", "INFO"]