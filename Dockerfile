# Docker Hub�ɂ���python�C���[�W���x�[�X�ɂ���
FROM python:3.6-alpine

# ���ϐ���ݒ肷��
#ENV PYTHONUNBUFFERED 1

# �R���e�i����code�f�B���N�g�������A���������[�N�f�B���N�g���Ƃ���
RUN mkdir /code
WORKDIR /code

# �z�X�gPC�ɂ���requirements.txt���R���e�i����code�f�B���N�g���ɃR�s�[����
# �R�s�[����requirements.txt���g���ăp�b�P�[�W���C���X�g�[������
ADD requirements.txt /code/
RUN apk --update-cache add python3-dev postgresql-client \
    gcc g++ libc-dev linux-headers postgresql-dev
RUN apk add sqlite
RUN pip install -r requirements.txt

# �z�X�gPC�̊e��t�@�C����code�f�B���N�g���ɃR�s�[����
ADD . /code/
