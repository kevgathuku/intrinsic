defmodule Intrinsic.Repo do
  use Ecto.Repo,
    otp_app: :intrinsic,
    adapter: Ecto.Adapters.Postgres
end
