from django.core.management.base import BaseCommand
import os 


#seems to only rename the directory still?

class Command(BaseCommand):
	help = 'Renames a Django project'


	def add_arguments(self, parser):
		parser.add_argument('new_project_name', type = str, help="Your new Django project name")


		#parser.add_argument('-p', '--prefix')
		#syntax here makes extra flag optional
		#-a for admin, just leave out for normal user

	def handle(self, *args, **kwargs):
		new_project_name = kwargs['new_project_name']


		#some logic for renaming project

		files_to_rename = ['/home/jawnothyn/django_dev/drydock/drjact_foundation/src/demo/settings/base.py', '/home/jawnothyn/django_dev/drydock/drjact_foundation/src/demo/wsgi.py',
		'/home/jawnothyn/django_dev/drydock/drjact_foundation/src/manage.py']
		folder_to_rename='demo'

		for f in files_to_rename:
			with open(f,'r') as file: 
				filedata = file.read()

			file = filedata.replace('demo', new_project_name)

			with open(f, 'w') as file:
				file.write(filedata)

		os.rename(folder_to_rename, new_project_name)

		self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % 
			new_project_name))