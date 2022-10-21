"""Provides a TrelloBoard class to manage boards in Trello"""
from main.core.api.http_methods import HttpMethods
from main.trello.api.trello_routes import TrelloApiRoutes
from main.core.api.request_manager import RequestManager

class TrelloOrganization:
    """Trello Organization requests
    """
    @staticmethod
    def create_organization(**Kwargs):
        """Method to create new organizations

        Args:
            displayName: The name to display for the Organization
        """
        endpoint_organization = TrelloApiRoutes.ORGANIZATIONS.value
        return RequestManager.get_instance().make_request(
            HttpMethods.POST.value,
            endpoint_organization, 
            **Kwargs
        )

    @staticmethod
    def get_organization(organization_id, **Kwargs):
        """Method to get an Organization information

        Args:
            organization_id (str): The ID or name of the Organization
        """
        endpoint_organization = f"{TrelloApiRoutes.ORGANIZATIONS.value}{organization_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_organization,
            **Kwargs
        )

    @staticmethod
    def update_organization(organization_id, **Kwargs):
        """Method to update an Organization information

        Args:
            organization_id (str): The ID or name of the Organization
        """
        endpoint_organization = f"{TrelloApiRoutes.ORGANIZATIONS.value}{organization_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_organization,
            **Kwargs
        )

    @staticmethod
    def delete_organization(organization_id):
        """Method to delete an organization

        Args:
            organization_id (str): The ID or name of the Organization
        """
        endpoint_organization = f"{TrelloApiRoutes.ORGANIZATIONS.value}{organization_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.DELETE.value,
            endpoint_organization
        )
    
    @staticmethod
    def update_organization_members(organization_id, **Kwargs):
        """Update an Organization's Members

        Args:
            organization_id (str): The ID or name of the Organization
            email (str): An email address
            fullName (str): Name for the member, at least 1 character not beginning or ending with a space
        """
        endpoint_organization = f"{TrelloApiRoutes.MEMBER_IN_ORGANIZATION.value}{organization_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_organization,
            **Kwargs
        )

    def get_organization_members(organization_id):
        """Get the Members of an Organization

        Args:
            organization_id (str): The ID or name of the Organization
        """
        endpoint_organization = f"{TrelloApiRoutes.MEMBER_IN_ORGANIZATION.value}{organization_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.GET.value,
            endpoint_organization,
        )
    
    def update_organization_member(organization_id, member_id, **Kwargs):
        """Update a specific Member of an Organization

        Args:
            organization_id (str): The ID or name of the Organization
            member_id (str): The ID of the member
        """
        endpoint_organization = f"{(TrelloApiRoutes.MEMBER_IN_ORGANIZATION.value).format(organization_id)}{member_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.PUT.value,
            endpoint_organization,
            **Kwargs
        )
        
    def delete_organization_member(organization_id, member_id):
        """Delete a specific Member of an Organization

        Args:
            organization_id (str): The ID or name of the Organization
            member_id (str): The ID of the member
        """
        endpoint_organization = f"{(TrelloApiRoutes.MEMBER_IN_ORGANIZATION.value).format(organization_id)}{member_id}"
        return RequestManager.get_instance().make_request(
            HttpMethods.DELETE.value,
            endpoint_organization
        )
    

