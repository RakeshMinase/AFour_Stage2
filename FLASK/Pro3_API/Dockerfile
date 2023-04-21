FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY ./Requirements.txt Requirements.txt
RUN pip install --no-cache-dir --upgrade -r Requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]