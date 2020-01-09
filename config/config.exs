# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :intrinsic,
  ecto_repos: [Intrinsic.Repo]

# Configures the endpoint
config :intrinsic, IntrinsicWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "rzcaCao45aQHq0TPQsk3RPXN3qBy7ovT3vJu6IMvdbZgNgZa4S3eP0j/jlnXkmQj",
  render_errors: [view: IntrinsicWeb.ErrorView, accepts: ~w(html json)],
  pubsub: [name: Intrinsic.PubSub, adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
