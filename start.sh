
if $1 = start ; then
  export DISPLAY=:20;

  /opt/local/bin/python2.7  get_session.py &
  sub_pid=$!
  echo $sub_pid >> prog.txt

  python command_control.py &
  sub_pid=$!
  echo $sub_pid >> prog.txt

  python startup_message.py

elif $1 = stop ; then
  IFS=$'\n'
  file=(`cat prog.txt`)

  kill "${file[1]}"
  kill "${file[2]}"

  echo "ぼったんサービスを終了しました"

else
  echo "引数を指定して下さい(start|stop)"
fi
