# This container defines a base boring mind machine image.
# This base container image will almost never be used.
FROM jfloff/alpine-python:recent-onbuild

RUN git clone -b prereleases/v23 https://github.com/rainbow-mind-machine/boring-mind-machine.git bmm
RUN cd /bmm && \
    /usr/bin/env pip install -r requirements.txt && \
    /usr/bin/env python /bmm/setup.py build && \
    /usr/bin/env python /bmm/setup.py install
