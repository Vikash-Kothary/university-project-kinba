arecord -f cd -t raw | oggenc - -r | ssh vagrant mplayer -
