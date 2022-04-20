# import sqlalchemy as sa
# from sqlalchemy.dialects.postgresql import JSONB

# from datetime import datetime
# from dateutil import tz

# from db.session import metadata

# user = sa.Table(
#     "user",
#     metadata,
#     sa.Column(
#         "uid",
#         sa.BIGINT,
#         primary_key=True,
#     ),
#     sa.Column("origin_id", sa.String, nullable=True),
#     sa.Column("platform", sa.String),
#     sa.Column("data", JSONB, nullable=False),
#     sa.Column("created_at", sa.TIMESTAMP,
#               default=lambda: datetime.now(tz=tz.UTC)),
#     sa.Column("edited_at", sa.TIMESTAMP,
#               default=lambda: datetime.now(tz=tz.UTC)),
#     sa.Column("times_edited", sa.INTEGER, default=lambda: 0)