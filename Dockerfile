FROM continuumio/Anaconda3:4.4.0
MAINTAINER UNP, https:// vatiktech.com
RUN MKDIR 
copy ./dockerfiles /app
EXPOSE 5000
WORKDIR /app/dockerfiles
RUN pip install -r requirements.txt
CMD python randomforestmodel_api.py