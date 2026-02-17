import { useUsers } from "../hooks/useUsers";
import UserCard from "./components/UserCard";

export default function Users() {
  const { users, loading } = useUsers();

  if (loading) return <p>Carregando...</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Lista de Usuários</h1>

      {users.length === 0 ? (
        <p>Nenhum usuário encontrado</p>
      ) : (
        users.map((user) => (
          <UserCard key={user.id} user={user} />
        ))
      )}
    </div>
  );
}
