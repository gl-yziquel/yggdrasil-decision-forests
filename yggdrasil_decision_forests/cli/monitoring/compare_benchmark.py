# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""Compares the csv generated by two runs of a benchmark.

Usage example:
  bazel run -c opt \
      //yggdrasil_decision_forests/cli/monitoring:compare_benchmark\
      -- --p1=/tmp/train_benchmark.csv --p2=/tmp/train_benchmark_new.csv
"""

from absl import app
from absl import flags
import pandas as pd

FLAGS = flags.FLAGS

flags.DEFINE_string("p1", "", "First csv file")
flags.DEFINE_string("p2", "", "Second csv file")


def main(argv) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  d1 = pd.read_csv(FLAGS.p1)
  d2 = pd.read_csv(FLAGS.p2)
  d1["new_training_time"] = d2["training_time"]

  d1["delta"] = (d1["new_training_time"] - d1["training_time"]) / d1[
      "training_time"
  ]
  print(d1)


if __name__ == "__main__":
  app.run(main)
