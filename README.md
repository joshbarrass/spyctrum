# spyctrum #

[![Build Status](https://api.travis-ci.com/joshbarrass/spyctrum.svg?branch=master)](https://travis-ci.com/joshbarrass/spyctrum)
[![Code Climate](https://codeclimate.com/github/joshbarrass/spyctrum/badges/gpa.svg)](https://codeclimate.com/github/joshbarrass/spyctrum)
[![Test Coverage](https://codeclimate.com/github/joshbarrass/spyctrum/badges/coverage.svg)](https://codeclimate.com/github/joshbarrass/spyctrum/coverage)
[![Issue Count](https://codeclimate.com/github/joshbarrass/spyctrum/badges/issue_count.svg)](https://codeclimate.com/github/joshbarrass/spyctrum)

My attempt to create a spectrum analyser.

------------------------------------------------------------

## What is Spyctrum?

**Spyctrum is still in active development! See the [Roadmap](#roadmap)
for details on the current progress.**

Spyctrum is intended to be a simple spectrum analyser written in
Python. My motivation for writing it lies primarily in music, as a
tool to aid in "reverse-engineering" music, however I want the project
to remain useful for other purposes, including spectral analysis of
scientific data and visualisation of music or other signals.

Spyctrum primarily uses numpy to perform Fourier analysis on small
chunks of your input signal. This allows you to examine the
frequencies present in a small time range, which, if you are
musically-motivated, should allow you to pick out the dominant notes
and associated harmonics in an audio signal to help in transcribing
music. If you struggle to recognise musical notes by ear, this could
be invaluable in learning to play a piece of music you can't find
suitable sheet music for.

## Supported Formats

The scipy module is used for converting audio data to numpy
arrays. This by default can only read .WAV files, but if you are only
intending to read .WAV files you will not require any external
software -- numpy and scipy will be sufficient. In order to provide
support for other formats, ffmpeg is used to convert tracks into a
format scipy can read. This can be done either in-memory or using
tempfiles. This means that spyctrum should support any format ffmpeg
supports, including most popular formats, such as MP3, OGG, AAC, FLAC,
etc.

## Roadmap

- [X] Implement reading of audio files
- [ ] Write a proper README about the project 
- [X] Fourier analysis functions
    - [ ] ~~Frequencies corresponding to musical notes~~ _This will be done at the histogram level by definining appropriate bins_
    - [x] Conversion between frequencies and musical notes
    - [X] Variable chunk size
    - [X] Variable chunk position
    - [ ] Apply window functions to a chunk
- [ ] Graphing functions
    - [ ] Musical notes on x-axis
    - [ ] Linear amplitude
    - [ ] Logarithmic amplitude (dB scale?)
- [ ] Peak identification
- [ ] Be useable as a module
- [ ] Playback from array
- [ ] Write a GUI
    - [ ] Graphs (linear and log amplitude)
    - [ ] Seekbar to select point of interest
    - [ ] Playback with live graphs
    - [ ] Mouse over bar on graph highlights the same note at different octaves
- [ ] Customisable spectrum animations
