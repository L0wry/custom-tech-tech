thisdir="$(realpath $PWD)"

docker run --rm \
  --name="sdet-test-mw" \
  --net="host" \
  --volume="$thisdir/screenshots/:/screenshots/" \
  --volume="$thisdir/sdet-test-submission.py:/main.py":ro \
  weihan/webdriver-python

