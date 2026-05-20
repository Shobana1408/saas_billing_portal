from models.company import Company


class CompanyService:

    @staticmethod
    def create_company(company_name, company_email, company_phone, company_address, industry, total_employees):
        Company.create(
            company_name=company_name,
            company_email=company_email,
            company_phone=company_phone,
            company_address=company_address,
            industry=industry,
            total_employees=total_employees
        )

        return {
            "status": True,
            "message": "Company created successfully"
        }

    @staticmethod
    def get_all_companies():
        return Company.get_all()

    @staticmethod
    def get_company_details(company_id):
        return Company.get_by_id(company_id)

    @staticmethod
    def update_company(company_id, company_name, company_email, company_phone, company_address, industry, total_employees):
        Company.update(
            company_id=company_id,
            company_name=company_name,
            company_email=company_email,
            company_phone=company_phone,
            company_address=company_address,
            industry=industry,
            total_employees=total_employees
        )

        return {
            "status": True,
            "message": "Company updated successfully"
        }

    @staticmethod
    def delete_company(company_id):
        Company.delete(company_id)

        return {
            "status": True,
            "message": "Company deleted successfully"
        }