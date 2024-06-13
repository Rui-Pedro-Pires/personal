import NewServiceForm from "../components/NewServiceForm";
import NavbarComponent from "../components/NavbarComponent";

function NewService()
{
    return (
        <>
            <NavbarComponent></NavbarComponent>
            <NewServiceForm></NewServiceForm>
        </>
    );
}

export default NewService