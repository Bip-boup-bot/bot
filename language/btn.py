import nextcord
from .set import set
class boutton(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Français", style = nextcord.ButtonStyle.gray)
  async def fr(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    set(interaction.user.id, 'fr')
    await interaction.response.edit_message(content="Language changé pour le français.", view=None)

  @nextcord.ui.button(label="English", style = nextcord.ButtonStyle.gray)
  async def en(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    set(interaction.user.id, 'en')
    await interaction.response.edit_message(content="The language has been changed to english.", view=None)
