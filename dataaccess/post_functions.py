from app import mongo
def push_to_document(collection, query, push_to, content_to_push):
	"""
		Function: Use when you want to push to a single document, or to an array.
		Parameters:
			-collection <string>: The collection name where push has to be made
			-query <dict>: Conditions to match documents for updating
			-push_to <string>: The key where content has to be pushed
			-content_to_push <dict or any other type>: If pushing to an embedded document, this is a dict. Otherwise, can be any type.
		Returns: 1 if update was made, 0 if not
	"""

	# check if collection exists
	if collection not in mongo.db.list_collection_names():
		return None

	db_collection = mongo.db[str(collection)]
	update_result = db_collection.update_one(
		query,
		{"$push": {push_to: content_to_push}}
	)
	return update_result.modified_count

def set_something(collection, query, what_to_set, set_value):
	"""
		Function: Use when you want to set single key of a document.
		Parameters:
			-collection <string>: The collection name where push has to be made
			-query <dict>: Conditions to match documents for updating
			-what_to_set <string>: The field which has to be set
			-set_value <value_type>: Value to set to the field
		Returns: 1 if update was made, 0 if not
	"""

	# check if collection exists
	if collection not in mongo.db.list_collection_names():
		return None

	db_collection = mongo.db[str(collection)]
	update_result = db_collection.update_one(
		query,
		{"$set": {what_to_set: set_value}}
	)
	return update_result.modified_count

def remove_from_list(collection, query, list_location, remove_value):
	"""
		Function: Use when you want to remove values from a list.
		Parameters:
			-collection <string>: The collection name where push has to be made
			-query <dict>: Conditions to match documents for updating
			-list_location <string>: The location of the list from where element is to be removed (for example: workflows_assigned.workflow_id.users)
			-remove_value <value_type>: Value to remove from the list.
		Returns: 1 if update was made, 0 if not
	"""

	# check if collection exists
	if collection not in mongo.db.list_collection_names():
		return None

	db_collection = mongo.db[str(collection)]
	update_result = db_collection.update_one(
		query,
		{"$pull": {list_location: remove_value}}
	)
	return update_result.modified_count

def remove_document(collection, query):
	# check if collection exists
	if collection not in mongo.db.list_collection_names():
		return None

	db_collection = mongo.db[str(collection)]
	result = db_collection.delete_one(query)
	return result.deleted_count