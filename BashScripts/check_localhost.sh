if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

if test -n $"PATH"; then
  echo "your path is not empty"
fi