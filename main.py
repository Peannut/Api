# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoukaddo <zoukaddo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/01 21:19:09 by zoukaddo          #+#    #+#              #
#    Updated: 2023/05/01 21:25:31 by zoukaddo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import *
import json, time

app = Flask(__name__)

@app.rout('/', methods=['GET'])
def home_page():
	data_set = {'Page':'Home','Message' :'Seccessfully loaded the Home page', 'Timestamp':time.time()}
	json_dump = json.dumps(data_set)

	return json_dump

@app.rout('/user', methods=['GET'])
def request_page():
	user_query = str(request.args.get('user')) 
	data_set = {'Page':'Home','Request' :'Seccessfully got the Request from {user_query}', 'Timestamp':time.time()}
	json_dump = json.dumps(data_set)

	return json_dump


if __name__ == '__main__':
	app.run(42)
