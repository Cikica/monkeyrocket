#!/usr/bin/env python

class Monkey_Command_Parser:

	def make(self, command, banana_information):
		
		if command['banana']:
			return self.make_definition_out_of_banana_command(command, banana_information)
			
		if command['rocket']:
			return self.make_definition_out_of_rocket_command(command, banana_information)

	def make_definition_out_of_rocket_command(self, command, banana):

		definition = self.make_action_definition({
			"name" : banana['name'],
			"url"  : banana['url']
		})

		if command['add']:
			return definition['rocket'][self.resolve_add_command_action(command, banana, "rocket" )]

		if command['remove']:
			if banana['is_active']:
				return definition['rocket']['deactivate']

			return definition['rocket']['nothing']


	def make_definition_out_of_banana_command(self, command, banana):

		action = self.resolve_add_command_action(command, banana, "banana")
		
		if command['add']:
			definition = self.make_action_definition({
				"name" : banana['name'],
				"url"  : banana['url']
			})

			return definition['rocket'][action]


		if command['remove']:
			if banana['is_active']:
				return definition['rocket']['deactivate']

			return definition['rocket']['nothing']

	def resolve_add_command_action(self, command, banana, type):

		if banana['is_active'] and banana['is_installed']:
			return "nothing"

		if banana['is_active'] == False and banana['is_installed']:
			return "nothing" if type == "banana" else "launch"

		if banana['is_installed'] == False and banana['is_known']:
			return "download" if type == "banana" else "download:launch"

		if command['<banana_url>'] != None:
			return "download" if type == "banana" else "download:launch"

		return "error"

	def make_action_definition(self, banana):
		return {
			"rocket" : {
				"nothing" : {
					"report" : {
						"text" : banana['name'] +" is already active"
					}
				},
				"launch" : {
					"launch_banana" : {
						"name" : banana['name']
					}
				},
				"download:launch" : {
					"prompt" : {
						"text"       : "Banana needs to be downloaded first before it can be launched, procceed?(y/n)",
						"is_true_if" : ["y", "yes", "Y", "Yes", "YES"],
						"if_true"    : {
							"download_banana" : {
								"name" : banana['name'],
								"url"  : banana['url'],
								"when_done"   : {
									"launch_banana" : {
										"name" : banana['name']
									},
								}
							}
						},
						"if_false"  : {
							"report" : {
								"text" : "Oke not goona do it."
							}
						}
					}
				},
				"deactivate" : {
					"deactivate_banana" : {
						"name" : banana['name']
					}
				},
				"error" : {
					"report" : {
						"text" : "The banana name is not known or downloaded and a valid banana url has not been provided so that it may be added."
					}
				}
			},
			"banana" : {},
		}
