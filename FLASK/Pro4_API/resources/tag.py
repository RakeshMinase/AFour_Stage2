from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import TagSchema, ItemAndTagSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from flask import request

from db import db
from models import TagModel, StoreModel, ItemModel

blp = Blueprint("Tags", "tags", description="Operations on tags")


@blp.route("/store/<string:store_id>/tag")
class TagsInStore(MethodView):
    @jwt_required()
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store_tags = StoreModel.query.get_or_404(store_id)
        return store_tags.tags.all()

    # @blp.arguments(TagSchema)
    @jwt_required()
    @blp.response(201, TagSchema)
    def post(self, store_id):
        tag_data = request.get_json()
        if TagModel.query.filter(
            TagModel.store_id == store_id, TagModel.tag_name == tag_data["tag_name"]
        ).first():
            abort(400, message="Tag name already exists in the store")
        tag = TagModel(**tag_data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=e)
        return tag


@blp.route("/tag/<string:tag_id>")
@jwt_required()
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @blp.response(
        202,
        description="Deletes a tag if no item is tagged with it",
        example={"message": "Tag Deleted"},
    )
    @blp.alt_response(404, description="Tag not found")
    @blp.alt_response(
        400, description="Tag is assigned to some item. In this case Tag is not deleted"
    )
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag Deleted"}
        abort(
            400,
            message="Couldnot delete the tag. Some item might be related to that tag",
        )


@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItems(MethodView):
    @jwt_required()
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        if item.store.id != tag.store.id:
            abort(
                400,
                message="Make sure that item and tag are belonging to same store before linking",
            )

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured while inserting the tags")
        return item

    @jwt_required()
    @blp.response(200, ItemAndTagSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured in deleteing the tag")

        return tag
