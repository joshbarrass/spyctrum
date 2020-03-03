# spyctrum #

[![Build Status](https://api.travis-ci.com/joshbarrass/spyctrum.svg?branch=master)](https://travis-ci.com/joshbarrass/spyctrum)
[![Code Climate](https://codeclimate.com/github/joshbarrass/spyctrum/badges/gpa.svg)](https://codeclimate.com/github/joshbarrass/spyctrum)
[![Test Coverage](https://codeclimate.com/github/joshbarrass/spyctrum/badges/coverage.svg)](https://codeclimate.com/github/joshbarrass/spyctrum/coverage)
[![Issue Count](https://codeclimate.com/github/joshbarrass/spyctrum/badges/issue_count.svg)](https://codeclimate.com/github/joshbarrass/spyctrum)

My attempt to create a spectrum analyser.

------------------------------------------------------------

## Roadmap

- [X] Implement reading of audio files
- [ ] Write a proper README about the project 
- [ ] Fourier analysis functions
    - [ ] Frequencies corresponding to musical notes
        - [ ] Conversion between frequencies and musical notes
    - [X] Variable chunk size
    - [X] Variable chunk position
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
