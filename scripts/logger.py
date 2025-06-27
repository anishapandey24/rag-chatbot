# scripts/logger.py
import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
