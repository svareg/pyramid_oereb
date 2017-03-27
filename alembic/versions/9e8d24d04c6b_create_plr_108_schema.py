"""create plr 108 schema

Revision ID: 9e8d24d04c6b
Revises:
Create Date: 2017-03-14 19:03:42.190050

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = '9e8d24d04c6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'authority',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('authority_web', sa.String(), nullable=True),
        sa.Column('uid', sa.String(length=12), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'document_base',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('text_web', sa.String(), nullable=True),
        sa.Column('legal_state', sa.String(), nullable=False),
        sa.Column('published_from', sa.Date(), nullable=False),
        sa.Column('type', sa.Unicode(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'view_service',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('link_wms', sa.String(), nullable=False),
        sa.Column('legend_web', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'document',
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('official_title', sa.String(), nullable=True),
        sa.Column('abbreviation', sa.String(), nullable=True),
        sa.Column('official_number', sa.String(), nullable=True),
        sa.Column('canton', sa.String(length=2), nullable=True),
        sa.Column('municipality', sa.Integer(), nullable=True),
        sa.Column('document', sa.Binary(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type', sa.Unicode(), server_default='document', nullable=True),
        sa.Column('authority_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['authority_id'], [u'plr_108.authority.id'], ),
        sa.ForeignKeyConstraint(['id'], [u'plr_108.document_base.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'legend_entry',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('symbol', sa.Binary(), nullable=False),
        sa.Column('legend_text', sa.String(), nullable=False),
        sa.Column('type_code', sa.String(length=40), nullable=False),
        sa.Column('type_code_list', sa.String(), nullable=False),
        sa.Column('topic', sa.String(), nullable=False),
        sa.Column('subtopic', sa.String(), nullable=True),
        sa.Column('additional_topic', sa.String(), nullable=True),
        sa.Column('view_service_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['view_service_id'], [u'plr_108.view_service.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'public_law_restriction',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('topic', sa.String(), nullable=False),
        sa.Column('subtopic', sa.String(), nullable=True),
        sa.Column('additional_topic', sa.String(), nullable=True),
        sa.Column('type_code', sa.String(length=40), nullable=True),
        sa.Column('type_code_list', sa.String(), nullable=True),
        sa.Column('legal_state', sa.String(), nullable=False),
        sa.Column('published_from', sa.Date(), nullable=False),
        sa.Column('view_service_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['view_service_id'], [u'plr_108.view_service.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'reference_definition',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('topic', sa.String(), nullable=True),
        sa.Column('canton', sa.String(length=2), nullable=True),
        sa.Column('municipality', sa.Integer(), nullable=True),
        sa.Column('authority_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['authority_id'], [u'plr_108.authority.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'article',
        sa.Column('number', sa.String(), nullable=False),
        sa.Column('text', sa.String(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type', sa.Unicode(), server_default='article', nullable=True),
        sa.Column('document_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['document_id'], [u'plr_108.document.id'], ),
        sa.ForeignKeyConstraint(['id'], [u'plr_108.document_base.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'document_hint',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('document_id', sa.Integer(), nullable=False),
        sa.Column('hint_document_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['document_id'], [u'plr_108.document.id'], ),
        sa.ForeignKeyConstraint(['hint_document_id'], [u'plr_108.document.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'document_reference_definition',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('document_id', sa.Integer(), nullable=False),
        sa.Column('reference_definition_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['document_id'], [u'plr_108.document.id'], ),
        sa.ForeignKeyConstraint(['reference_definition_id'],
                                [u'plr_108.reference_definition.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'geometry',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('legal_state', sa.String(), nullable=False),
        sa.Column('published_from', sa.Date(), nullable=False),
        sa.Column('geo_metadata', sa.String(), nullable=True),
        sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=21781),
                  nullable=True),
        sa.Column('public_law_restriction', sa.Integer(), nullable=False),
        sa.Column('authority_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['authority_id'], [u'plr_108.authority.id'], ),
        sa.ForeignKeyConstraint(['public_law_restriction'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'legal_provision',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type', sa.Unicode(), server_default='legal_provision', nullable=True),
        sa.ForeignKeyConstraint(['id'], [u'plr_108.document.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'public_law_restriction_base',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('public_law_restriction_id', sa.Integer(), nullable=False),
        sa.Column('public_law_restriction_base_id', sa.Integer(), nullable=False),
        sa.Column('authority_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['authority_id'], [u'plr_108.authority.id'], ),
        sa.ForeignKeyConstraint(['public_law_restriction_base_id'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.ForeignKeyConstraint(['public_law_restriction_id'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'public_law_restriction_document',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('public_law_restriction_id', sa.Integer(), nullable=False),
        sa.Column('document_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['document_id'], [u'plr_108.document_base.id'], ),
        sa.ForeignKeyConstraint(['public_law_restriction_id'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    op.create_table(
        'public_law_restriction_refinement',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('public_law_restriction_id', sa.Integer(), nullable=False),
        sa.Column('public_law_restriction_base_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['public_law_restriction_base_id'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.ForeignKeyConstraint(['public_law_restriction_id'],
                                [u'plr_108.public_law_restriction.id'], ),
        sa.PrimaryKeyConstraint('id'),
        schema='plr_108'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('public_law_restriction_refinement', schema='plr_108')
    op.drop_table('public_law_restriction_document', schema='plr_108')
    op.drop_table('public_law_restriction_base', schema='plr_108')
    op.drop_table('legal_provision', schema='plr_108')
    op.drop_table('geometry', schema='plr_108')
    op.drop_table('document_reference_definition', schema='plr_108')
    op.drop_table('document_hint', schema='plr_108')
    op.drop_table('article', schema='plr_108')
    op.drop_table('reference_definition', schema='plr_108')
    op.drop_table('public_law_restriction', schema='plr_108')
    op.drop_table('legend_entry', schema='plr_108')
    op.drop_table('document', schema='plr_108')
    op.drop_table('view_service', schema='plr_108')
    op.drop_table('document_base', schema='plr_108')
    op.drop_table('authority', schema='plr_108')
    # ### end Alembic commands ###