FROM dipintimanandhar/ubuntum20cs020:v1
WORKDIR /app
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["Application.py"]