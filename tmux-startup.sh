#!/bin/sh

tmux kill-session


tmux new-session -d -s main -n osc /bin/bash
tmux set -g mouse on

#tmux new-window -d -t '=main' -n osc 
tmux send-keys -t '=main:=osc' 'cd /home/pi/gith/m5stack-display' Enter
tmux send-keys -t '=main:=osc' 'python3 osc-nowplaying.py' Enter

tmux new-window -d -t '=main' -n lora 
tmux send-keys -t '=main:=lora' 'cd /home/pi/gith/lora_comm' Enter
tmux send-keys -t '=main:=lora' 'python3 outdoor_server.py' Enter

