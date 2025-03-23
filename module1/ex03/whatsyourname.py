# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatsyourname.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aalawad <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/23 11:37:39 by aalawad           #+#    #+#              #
#    Updated: 2025/03/23 11:54:17 by aalawad          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print('What is your first name?...', end=" ")
first_name = input()
print('What is your last name?...', end=" ")
last_name = input()
first_name = first_name.strip()
last_name = last_name.strip()
message = "Happy to have you in my computer " + first_name + " " + last_name + "!"
print(message)
