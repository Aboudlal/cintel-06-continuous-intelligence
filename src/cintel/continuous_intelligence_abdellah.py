"""continuous_intelligence_abdellah.py - Custom Project script.

Author: Abdellah Boudlal
Date: 2026-04

Custom continuous intelligence project.

This script reads system metrics, creates useful signals,
detects anomalies, summarizes system performance,
and saves the final assessment to an artifact file.
"""

import logging
from pathlib import Path
from typing import Final

import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

LOG: logging.Logger = get_logger("P6CUSTOM", level="DEBUG")

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_case.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "system_assessment_abdellah.csv"

MAX_ERROR_RATE: Final[float] = 0.05
MAX_AVG_LATENCY: Final[float] = 40.0
MIN_PERFORMANCE_SCORE: Final[float] = 0.95


def main() -> None:
    """Run the custom pipeline."""
    log_header(LOG, "CINTEL CUSTOM")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # STEP 1: READ DATA
    df = pl.read_csv(DATA_FILE)
    LOG.info(f"STEP 1. Loaded {df.height} system records")

    # STEP 2: DESIGN SIGNALS
    LOG.info("STEP 2. Designing signals from raw metrics...")

    df = df.with_columns(
        [
            (pl.col("errors") / pl.col("requests")).alias("error_rate"),
            (pl.col("total_latency_ms") / pl.col("requests")).alias("avg_latency_ms"),
            (pl.col("requests") - pl.col("errors")).alias("successful_requests"),
        ]
    )

    df = df.with_columns(
        [
            (pl.col("successful_requests") / pl.col("requests")).alias(
                "performance_score"
            )
        ]
    )

    # STEP 3: DETECT ANOMALIES
    LOG.info("STEP 3. Checking for anomalies in system signals...")

    anomalies_df = df.filter(
        (pl.col("error_rate") > MAX_ERROR_RATE)
        | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        | (pl.col("performance_score") < MIN_PERFORMANCE_SCORE)
    )

    LOG.info(
        f"STEP 3. Using thresholds: MAX_ERROR_RATE={MAX_ERROR_RATE}, "
        f"MAX_AVG_LATENCY={MAX_AVG_LATENCY}, "
        f"MIN_PERFORMANCE_SCORE={MIN_PERFORMANCE_SCORE}"
    )

    LOG.info(f"STEP 3. Anomalies detected: {anomalies_df.height}")

    # STEP 4: SUMMARIZE SYSTEM STATE
    LOG.info("STEP 4. Summarizing system state from monitored signals...")

    summary_df = df.select(
        [
            pl.col("requests").mean().alias("avg_requests"),
            pl.col("errors").mean().alias("avg_errors"),
            pl.col("error_rate").mean().alias("avg_error_rate"),
            pl.col("avg_latency_ms").mean().alias("avg_latency_ms"),
            pl.col("performance_score").mean().alias("avg_performance_score"),
        ]
    )

    summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > MAX_ERROR_RATE)
            | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
            | (pl.col("avg_performance_score") < MIN_PERFORMANCE_SCORE)
        )
        .then(pl.lit("DEGRADED"))
        .otherwise(pl.lit("STABLE"))
        .alias("system_state")
    )

    LOG.info("STEP 4. System assessment completed")

    # STEP 5: SAVE RESULT
    summary_df.write_csv(OUTPUT_FILE)
    LOG.info(f"STEP 5. Wrote system assessment file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


if __name__ == "__main__":
    main()
