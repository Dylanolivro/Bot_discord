    # @app_commands.command(name="addition", description="Additionne 2 nombres")
    # async def addition_slash(self, interaction: discord.Interaction, nombre1 : float, nombre2: float):
    #     nombre1 = int(nombre1) if nombre1.is_integer() else nombre1
    #     nombre2 = int(nombre2) if nombre2.is_integer() else nombre2
    #     result = nombre1 + nombre2
    #     result = int(result) if result.is_integer() else result
    #     await interaction.response.send_message(f"Le résultat de l'équation {nombre1} + {nombre2} est {result}", ephemeral=True)


def addition(nb1: float, x:str = "+", nb2:float):
    result = nb1 + x + nb2
    return result


print(addition(2.323,2))

def addition(nb1: float, x: str = "+", nb2: float):
    if x not in ["+", "-", "*", "/"]:
        raise ValueError("L'opérateur doit être +, -, * ou /")

    if x == "+":
        result = nb1 + nb2
    elif x == "-":
        result = nb1 - nb2
    elif x == "*":
        result = nb1 * nb2
    elif x == "/":
        if nb2 != 0:
            result = nb1 / nb2
        else:
            raise ValueError("La division par zéro n'est pas autorisée")

    return result
