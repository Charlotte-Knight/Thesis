#!/usr/bin/env bash

killall lualatex
killall latex

rm tikz/*
touch tikz/boo

cp thesis.tex /tmp/
cp thesis.bib /tmp/
cp thesis.sty /tmp/
rm thesis*
mv /tmp/thesis.tex .
mv /tmp/thesis.bib .
mv /tmp/thesis.sty .
